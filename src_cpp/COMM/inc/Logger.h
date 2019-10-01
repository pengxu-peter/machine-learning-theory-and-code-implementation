//
//  @ Project : SanqiNet
//  @ File Name : Logger.h
//  @ Date : 2019/10/1
//  @ Author : xupeng (pengxu_peter@foxmail.com)
//

#if !defined(_LOGGER_H)
#define _LOGGER_H


namespace SANQI {
	namespace COMM {
		class Logger {
		public:
			static log4cplus::Logger m_rootLog;
			~Logger();
			static std::share_ptr<Logger> getInstance();
		private:
			std::share_ptr<Logger> m_logger;
			Logger();
			Logger(const Logger & _logger);
		};
	}
}

#endif  //_LOGGER_H
