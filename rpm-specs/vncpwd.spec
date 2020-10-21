%global         gituser         jeroennijhof
%global         gitname         vncpwd
%global         commit          596854c237e26b3f615d933e8abd040f1ed9b5c9
%global         commitdate      20170607
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           vncpwd
Version:        0.0
Release:        8.%{commitdate}git%{shortcommit}%{?dist}
Summary:        VNC Password Decrypter

License:        GPLv3
URL:            https://github.com/jeroennijhof/vncpwd

Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# https://github.com/jeroennijhof/vncpwd/issues/4
Patch0:         %{name}-make.patch
# https://github.com/jeroennijhof/vncpwd/issues/6
Patch1:         %{name}-unsigned.patch

BuildRequires:  gcc

%description
The vncpwd decrypts the VNC password.

%prep
%setup -q -n %{name}-%{commit}
%patch0 -p 1 -b .make
%patch1 -p 1 -b .unsigned



%build
%make_build CFLAGS="%{optflags}"



%install
make install DESTDIR="%{buildroot}"



%files
%doc README
%license LICENSE
%{_bindir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-8.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-7.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-6.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-5.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-4.20170607git596854c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Dec 10 2017 Michal Ambroz <rebus at, seznam.cz> 0.0-3.20170607git596854c
- bump to latest commit
- upstream notified about wrong FSF address
- https://github.com/jeroennijhof/vncpwd/issues/3

* Thu Apr 13 2017 Michal Ambroz <rebus at, seznam.cz> 0.0-2.gitdafebe0
- removed unused macro, adding README as license file

* Sat Mar 18 2017 Michal Ambroz <rebus at, seznam.cz> 0.0-1.gitdafebe0
- initial build for Fedora
