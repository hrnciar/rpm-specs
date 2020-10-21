Summary: High-performance implementation of a colorful cat
Name:    lolcat
Version: 1.0
Release: 8%{?dist}
Source:  https://github.com/jaseg/lolcat/archive/v%{version}/%{name}-%{version}.tar.gz
URL:     https://github.com/jaseg/lolcat/

Patch1:  lolcat-Makefile.patch

License: WTFPL
BuildRequires: make
BuildRequires: gcc

%description
lolcat is a colorful version of 'cat'. It is faster than python-lolcat 
and much faster than ruby-lolcat. It works well with "non-binary" 
characters, but who would want to display binary data!

%prep
%autosetup

%build
%set_build_flags
%make_build all

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
%make_install DESTDIR=$RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/lolcat
%{_bindir}/censor
%doc README.md
%license LICENSE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 josef radinger <cheese@nosuchhost.net> - 1.0-6
- modify description

* Mon Aug 26 2019 josef radinger <cheese@nosuchhost.net> - 1.0-5
- use a better source-url
- use %%autosetup
- use %%make_build
- use %%make_install (plus patch1 to preserve timestamps)
- better Summary

* Sat Aug 17 2019 josef radinger <cheese@nosuchhost.net> - 1.0-4
- use %%{_bindir} instead of /usr/bin
- invoke %%set_build_flags before make

* Fri Aug 16 2019 josef radinger <cheese@nosuchhost.net> - 1.0-3
- correct license
- small cleanup in spec-file

* Wed Aug 07 2019 josef radinger <cheese@nosuchhost.net> - 1.0-2
- add URL

* Tue Aug 06 2019 josef radinger <cheese@nosuchhost.net> - 1.0-1
- initial package

