%global gittag 1.0.3
%global debug_package %{nil}

Name: pwkickstart
Version: %{gittag}
Release: 7%{?dist}
Summary: Helps to generate kickstart passwords
License: MIT
URL: https://github.com/lzap/pwkickstart
Source0: https://github.com/lzap/%{name}/archive/%{gittag}.tar.gz

Requires:	python3

BuildRequires:	txt2man

%description
Helps to generate kickstart passwords, similarly to grub-crypt tool.

%prep
%autosetup -n %{name}-%{gittag}

%build
txt2man -t %{name} -r %{version} -s 1 README > %{name}.1

%install
install -m 755 -D %{name} %{buildroot}/%{_bindir}/%{name}
install -m 644 -D %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.3-1
- Rebased to new upstream version

* Mon Feb 12 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.2-1
- Rebased to new upstream version
- Changed to python3 explicit dependency

* Mon Feb 12 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.1-1
- Initial version
