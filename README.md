 < void Exceptions::throw_stack_overflow_exception(Thread* THREAD, const char* file, int line) {
203 <   Handle exception;
204 <   if (!THREAD->has_pending_exception()) {
205 <     klassOop k = SystemDictionary::StackOverflowError_klass();
206 <     oop e = instanceKlass::cast(k)->allocate_instance(CHECK);
207 <     exception = Handle(THREAD, e);  // fill_in_stack trace does gc
208 <     assert(instanceKlass::cast(k)->is_initialized(), "need to increase min_stack_allowed calculation");
209 <   } else {
210 <     // if prior exception, throw that one instead
211 <     exception = Handle(THREAD, THREAD->pending_exception());
212 <   }
213 <   _throw(THREAD, file, line, exception);
214 < }


 // fy
221 <   static void throw_stack_overflow_exception(Thread* thread, const char* file, int line);
