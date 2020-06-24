Name:           keyrings-filesystem
Version:        1
Release:        12%{?dist}
Summary:        Keyrings filesystem layout

License:        Public Domain
BuildArch:      noarch

Requires:       filesystem
Requires:       rpm

%description
This package provides the directory to store keyrings.

%prep
# Nothing to prep


%build
# Nothing to build


%install
# Directories
install -d %{buildroot}%{_rpmconfigdir}/macros.d
install -d %{buildroot}%{_datadir}/keyrings

# RPM macro
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.keyrings <<EOF
%%_keyringsdir %%_datadir/keyrings
EOF

%files
%dir %{_datadir}/keyrings
%{_rpmconfigdir}/macros.d/macros.keyrings


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Sandro Mani <manisandro@gmail.com> - 1-2
- Install macros in %%{_rpmconfigdir}/macros.d

* Mon Sep 23 2013 Sandro Mani <manisandro@gmail.com> - 1-1
- Initial package
