function [posit_x] = Mid2Max(x,best)
    M = max(abs(x-best));
    posit_x = 1 - abs(x-best) / M;
end

% % ע�⣺�����ļ������ο���һ����Ҫֱ�������Լ�����ģ������
% % �����������ĵĲ���Ҫ��ǳ��ϸ񣬴�����ͬҲ������Ϯ
% % ��Ƶ���ᵽ�ĸ��������ۺ�Ⱥ��������յ����Ǹ��е��Ʊʼ����м��뷽ʽ����Ⱥ�ļ������ء��������塢���롢�������ҵ������Ƶ���Ƽ������ϵȡ�
% % ��ע�ҵ�΢�Ź��ںš���ѧ��ģѧϰ����������̨���͡������������֣��ɻ�ó����Ľ�ģ�������ط��������͡����ݡ������֣��ɻ�ý�ģ���ݵĻ�ȡ���������͡���ͼ�������֣��ɻ����ѧ��ģ�г����Ļ�ͼ���������⣬Ҳ���Կ������ںŵ���ʷ���£����淢���Ķ��ǶԴ���а����ļ��ɡ�
% % ����������ʾ�ѡ����ѧ��ģ���ϣ��ɹ�ע�ҵ�΢�Ź��ںš���ѧ��ģѧϰ���������ں�̨���͡�������ּ��ɽ������(�ҵ�΢���ַ��https://weidian.com/?userid=1372657210)���й���
% % ��Ƶ�۸񲻹󣬵���ֵ�ܸߡ����˹���ۿ�ֻ��Ҫ58Ԫ�����˹����˾�����46Ԫ����Ƶ����Ҳ�����ص����عۿ��ģ��������Ҳ�Ҫ�ַ�֪ʶ��Ȩ������Ƶ�������Ͻ��ж������ۡ�
% % ����޸Ĵ��������صķ�����https://www.bilibili.com/video/av59423231���ؿ���