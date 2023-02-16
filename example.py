class NetworkFlowAnalytics:
    def __init__(self, flows):
        self.flows = flows

    @property
    def flow_duration(self):
        return sum([flow.end_time - flow.start_time for flow in self.flows])

    @property
    def total_packets_forward(self):
        return sum([packet.size for flow in self.flows for packet in flow.packets if packet.direction == 'forward'])

    @property
    def max_packet_size_backward(self):
        return max([packet.size for flow in self.flows for packet in flow.packets if packet.direction == 'backward'],
                   default=0)

    @property
    def avg_time_between_flows(self):
        flow_start_times = [flow.start_time for flow in self.flows]
        flow_start_times.sort()
        time_differences = [flow_start_times[i + 1] - flow_start_times[i] for i in range(len(flow_start_times) - 1)]
        return sum(time_differences) / len(time_differences)

    @property
    def max_time_between_packets_backward(self):
        packet_timestamps = [packet.timestamp for flow in self.flows for packet in flow.packets if
                             packet.direction == 'backward']
        packet_timestamps.sort()
        time_differences = [packet_timestamps[i + 1] - packet_timestamps[i] for i in range(len(packet_timestamps) - 1)]
        return max(time_differences, default=0)

    @property
    def mean_flow_active_time(self):
        flow_active_times = [flow.end_time - flow.start_time for flow in self.flows]
        return sum(flow_active_times) / len(flow_active_times)

    @property
    def stddev_packet_size(self):
        packet_sizes = [packet.size for flow in self.flows for packet in flow.packets]
        mean = sum(packet_sizes) / len(packet_sizes)
        variance = sum([(size - mean) ** 2 for size in packet_sizes]) / len(packet_sizes)
        return variance ** 0.5

    @property
    def median_packet_length(self):
        packet_sizes = [packet.size for flow in self.flows for packet in flow.packets]
        packet_sizes.sort()
        length = len(packet_sizes)
        if length % 2 == 0:
            return (packet_sizes[length // 2 - 1] + packet_sizes[length // 2]) / 2
        else:
            return packet_sizes[length // 2]
