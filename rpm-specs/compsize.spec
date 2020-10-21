Name:           compsize
Version:        1.3
Release:        4%{?dist}
Summary:        Utility for measuring compression ratio of files on btrfs
License:        GPLv2+
URL:            https://github.com/kilobyte/compsize
Source:         https://github.com/kilobyte/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  btrfs-progs-devel

%description
compsize takes a list of files (given as arguments) on a btrfs filesystem and
measures used compression types and effective compression ratio, producing
a report.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Thu Aug 06 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.3-4
- Use set_build_flags macro

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.3-1
- Version 1.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1-1
- Initial release
