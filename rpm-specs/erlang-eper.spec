%global realname eper
%global upstream massemanet


Summary:        Erlang Performance and Debugging Tools
Name:           erlang-%{realname}
Version:        0.99.1
Release:        6%{?dist}
BuildArch:	noarch
License:        MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:         eper-0001-unbundle-getopt.patch
Patch2:		eper-0002-Start-network-subsystem.patch
BuildRequires:  erlang-rebar


%description
This is a loose collection of Erlang Performance related tools:

 * dtop  - similar to unix top
 * ntop   - visualizes network traffic
 * atop   - shows various aspects of the VM allocators
 * redbug - similar to the OTP dbg application, but safer, better etc.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}

install -d %{buildroot}%{erlang_appdir}/priv/bin
install -p -m 0755 priv/bin/{dtop,ntop,redbug} %{buildroot}%{erlang_appdir}/priv/bin


%check
%{erlang_test}


%files
%doc AUTHORS README.md doc/redbug.txt doc/watchdog.txt
%license COPYING
%{erlang_appdir}/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.99.1-3
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.99.1-1
- Ver. 0.99.1

* Wed Feb 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.97.3-9
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.97.3-6
- Rebuild for Erlang 20 (with proper builddeps)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.97.3-1
- Ver. 0.97.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.97.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 25 2015 Filip Andres <filip@andresovi.net> - 0.97.1-1
- Ver. 0.97.1

* Wed Jul 08 2015 Filip Andres <filip@andresovi.net> - 0.90.0-1
- Ver. 0.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-8.20120621git16bae32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-7.20120621git16bae32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-6.20120621git16bae32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-5.20120621git16bae32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-4.20120621git16bae32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-3.20120621git16bae32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.60-2.20120621git16bae32
- Latest git tag
- Minor spec cleanups

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.60-1.20120501git592ef2
- Ver. 0.60.gitc592ef2
