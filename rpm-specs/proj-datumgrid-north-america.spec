Name:           proj-datumgrid-north-america
Version:        1.4
Release:        2%{?dist}
Summary:        North American datum shift grids for Proj

# See README.NORTHAMERICA
License:        CC-BY and OGL and Public Domain
URL:            https://proj4.org
Source0:        https://download.osgeo.org/proj/%{name}-%{version}.tar.gz

BuildArch:      noarch

Enhances:       proj

%description
This package contains additional North American datum shift grids for
Proj.


%prep
%autosetup -c


%install
install -dpm 0755 %{buildroot}%{_datadir}/proj
install -pm 0644 * %{buildroot}%{_datadir}/proj


%files
%doc README.NORTHAMERICA
%license README.NORTHAMERICA
%{_datadir}/proj/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3-1
- Update to latest version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1-1
- Initial package
