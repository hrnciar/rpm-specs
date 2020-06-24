%define luaver 5.3
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
#%global commit 6b358619032b1a7f0432ae56a2a9504738b2f953
#%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lua-wsapi
Version:        1.6.1
Release:        11%{?dist}
Summary:        Lua Web Server API

License:        MIT
URL:            http://keplerproject.github.com/wsapi/
# https://github.com/keplerproject/wsapi/archive/v1.6.1.tar.gz
Source0:        wsapi-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua(abi) = %{luaver}
BuildRequires:  dos2unix
Requires:       lua(abi) = %{luaver}
Requires:       lua-coxpcall

%description
WSAPI is an API that abstracts the web server from Lua web applications. By
coding against WSAPI your application can run on any of the supported servers
and interfaces (currently CGI, FastCGI and Xavante, on Windows and UNIX-based
systems).

WSAPI provides a set of helper libraries that help with request processing
and output buffering. You can also write applications that act as filters that
provide some kind of service to other applications, such as authentication,
file uploads, request isolation, or multiplexing.

WSAPI's main influence is Ruby's Rack framework, but it was also influenced by
Python's WSGI (PEP 333). It's not a direct clone of either of them, though,
and tries to follow standard Lua idioms.

%prep
%setup -q -n wsapi-%{version}


%build
dos2unix src/launcher/wsapi.cgi


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{luapkgdir}
mkdir -p %{buildroot}/var/www/cgi-bin/wsapi
make install LUA_DIR=%{buildroot}%{luapkgdir} BIN_DIR=%{buildroot}/var/www/cgi-bin/wsapi



%files
%doc README doc/us/*
%{luapkgdir}/*
%dir /var/www
%dir /var/www/cgi-bin
/var/www/cgi-bin/*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.6.1-2
- rebuild for lua 5.3

* Wed Oct 01 2014 Tim Niemueller <tim@niemueller.de> - 1.6.1-1
- Upgrade to 1.6.1, required to actually work with Xavante

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3.git6b35861
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2.git6b35861
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Tom Callaway <spot@fedoraproject.org> - 1.5-1.git6b35861
- update to 1.5 (git trunk) for lua 5.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Tim Niemueller <tim@niemueller.de> - 1.3.4-4
- Require lua-coxpcall, fixes #666090

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 23 2010 Tim Niemueller <tim@niemueller.de> - 1.3.4-2
- Own /var/www and /var/www/cgi-bin

* Wed Oct 20 2010 Tim Niemueller <tim@niemueller.de> - 1.3.4-1
- Initial package
