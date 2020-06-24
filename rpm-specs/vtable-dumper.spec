Name:           vtable-dumper
Version:        1.2
Release:        10%{?dist}
Summary:        Tool to list content of virtual tables in a C++ shared library

License:        GPL+ or LGPLv2+
URL:            https://github.com/lvc/vtable-dumper
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc gcc-c++
BuildRequires:  elfutils-libelf-devel


%description
Vtable-Dumper is a tool to list content of virtual tables in a C++ shared
library. It is intended for developers of software libraries and maintainers of
Linux distributions who are interested in ensuring backward binary
compatibility.


%prep
%autosetup


%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/


%files
%license LICENSE
%doc README
%{_bindir}/%{name}


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct  9 2016 Ville SkyttÃ¤ <ville.skytta@iki.fi> - 1.2-2
- Build with $RPM_OPT_FLAGS and $RPM_LD_FLAGS

* Thu Oct  6 2016 Richard Shaw <hobbes1069@gmail.com> - 1.2-1
- Update to latest upstream release.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Richard Shaw <hobbes1069@gmail.com> - 1.1-1
- Initial packaging.
