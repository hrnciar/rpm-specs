Name:		smtpping
Version:	1.1.3
Release:	9%{?dist}
Summary:	Small tool for measuring SMTP parameters

License:	GPLv2+
URL:		https://github.com/halonsecurity/smtpping
Source0:	https://github.com/halonsecurity/smtpping/archive/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	coreutils
BuildRequires:	gcc-c++
BuildRequires:	make

%description
A simple, portable tool for measuring SMTP server delay,
delay variation and throughput.

%prep
%setup -q

%build
mkdir -p build
cd build

%cmake .. -DMAN_INSTALL_DIR:PATH=%{_mandir}

make %{?_smp_mflags}

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.md
%{_mandir}/man1/*.1*
%{_bindir}/smtpping


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 25 2016 Denis Fateyev <denis@fateyev.com> - 1.1.3-1
- Update to 1.1.3 release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Denis Fateyev <denis@fateyev.com> - 1.1.2-2
- Spec improvements

* Thu Dec 10 2015 Denis Fateyev <denis@fateyev.com> - 1.1.2-1
- Initial release
