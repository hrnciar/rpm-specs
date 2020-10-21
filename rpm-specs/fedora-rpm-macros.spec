Name:           fedora-rpm-macros
Version:        26
Release:        9%{?dist}
Summary:        Miscellaneous Fedora RPM macros

License:        GPLv2+
Source0:        macros.fedora

BuildArch:      noarch

%description
This package contains the miscellaneous Fedora-related RPM macros.

%prep
echo <<END
%install_file 0 %{_rpmconfigdir}/macros.d/macros.fedora
END

%install
# Can't use %%rpmmacrodir or %%install_src yet.
install -D -m 644 %{SOURCE0} %{buildroot}/%{_rpmconfigdir}/macros.d/macros.fedora


%files
%{_rpmconfigdir}/macros.d/macros.fedora


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 26-1
- Initial package.
