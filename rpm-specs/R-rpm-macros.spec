Name:           R-rpm-macros
Version:        1.2.0
Release:        2%{?dist}
Summary:        Macros to help produce R packages

License:        MIT
URL:            https://github.com/rpm-software-management/R-rpm-macros
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       R-core
Requires:       rpm

%description
This package contains the R RPM macros, that most implementations should rely
on.

You should not need to install this package manually as the R-devel package
requires it. So install the R-devel package instead.


%prep
%autosetup -p1


%install
%make_install PREFIX=%{_prefix}


%files
%doc README.md
%license LICENSE
%{_rpmconfigdir}/fileattrs/R.attr
%{_rpmconfigdir}/R-deps.R


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Add R(ABI) dependency generation

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-2
- rebuilt

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version
- Always add R-core to automatic dependencies

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Initial package
