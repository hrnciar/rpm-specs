Name: smcalc
Summary: Matrix Calculator
URL: http://smcalc.sourceforge.net
Version: 1.0.1
Release: 4%{?dist}
Source0: https://sourceforge.net/projects/smcalc/files/smcalc/%{name}-%{version}.tar.gz
License: MIT

BuildRequires: gcc-c++

%description
Simple matrix calculator with TUI able to
do basic matrix operations including fast
computing of determinant.

%prep
%autosetup -n %{name}-%{version}
sed -i s:/usr/local:%{buildroot}%_prefix:g src/Makefile
sed -i 's:-ansi:-ansi -g:g' src/Makefile

%build
cd src
%make_build

%install
cd src
%make_install

%files
%license COPIYNG
%doc AUTHORS Changelog README
%{_bindir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.1-2
- Force enable debugger

* Mon Apr 10 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.1-1
- Initial
