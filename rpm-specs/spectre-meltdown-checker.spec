Name:       spectre-meltdown-checker
Version:    0.43
Release:    3%{?dist}

Summary:    Spectre & Meltdown vulnerability/mitigation checker for Linux
License:    GPLv3
URL:        https://github.com/speed47/spectre-meltdown-checker
Source0:    https://github.com/speed47/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   /bin/sh
Requires:   binutils
Requires:   coreutils
Requires:   gawk
Requires:   gzip
Requires:   grep
Requires:   sed
%if 0%{?rhel} == 6
Requires:   module-init-tools
Requires:   util-linux-ng
%else
Requires:   kmod
Requires:   util-linux
%endif

BuildRequires: help2man

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{name} -n "Spectre and Meltdown mitigation detection tool" \
    --no-info --output=%{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README.md
%{_bindir}/*
%{_mandir}/man1/%{name}*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.43-1
- Update to 0.43

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.42-1
- Update to 0.42

* Wed May 15 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.41-1
- Update to 0.41

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.40-1
- Update to 0.40

* Mon Aug 13 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.39-1
- Update to 0.39

* Tue Aug 07 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.38-1
- Update to 0.38

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.37-1
- Update to 0.37

* Tue Apr 03 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.36-1
- Update to 0.36

* Sun Feb 18 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.35-1
- Update to 0.35

* Tue Feb 13 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 0.34-1
- Update to 0.34

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.33-1
- Initial package
