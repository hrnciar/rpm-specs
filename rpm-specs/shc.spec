%global owner neurobin

Name: shc
Summary: Shell script compiler
URL: https://neurobin.org/projects/softwares/unix/shc/
Version: 4.0.3
Release: 3%{?dist}
Source0: https://github.com/%{owner}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License: GPLv3
BuildRequires: gcc

%description
SHC is a generic shell script compiler. It takes
a script, which is specified on the command line
and produces C source code. The generated source
code is then compiled and linked to produce a s-
tripped binary. 

%prep
%autosetup -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README README.md
%{_bindir}/%{name}
%{_mandir}/*/%{name}*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 9 2019 Mosaab Alzoubi <moceap@hotmail.com> - 4.0.3-1
- Update to 4.0.3

* Mon Apr 10 2017 Mosaab Alzoubi <moceap@hotmail.com> - 3.9.3-1
- Initial
