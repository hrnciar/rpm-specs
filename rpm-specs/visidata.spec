%global srcname visidata

Name:           %{srcname}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Terminal interface for exploring and arranging tabular data

License:        GPLv3
URL:            https://visidata.org
Source0:        %pypi_source
# https://github.com/saulpw/visidata/pull/269
Patch0001:      0001-Remove-extra-copy-of-man-page.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3-%{srcname} = %{version}-%{release}

%description
VisiData is an interactive multitool for tabular data. It combines the clarity
of a spreadsheet, the efficiency of the terminal, and the power of Python, into
a lightweight utility which can handle millions of rows with ease.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

# Optional dependencies
Recommends: python3dist(PyYAML)
Recommends: python3dist(datapackage)
Recommends: python3dist(dnslib)
Recommends: python3dist(dpkt)
Recommends: python3dist(fonttools)
Recommends: python3dist(h5py)
Recommends: python3dist(lxml)
Recommends: python3dist(mapbox-vector-tile)
Recommends: python3dist(namestand)
Recommends: python3dist(numpy)
Recommends: python3dist(openpyxl)
Recommends: python3dist(pandas) >= 0.19.2
Recommends: python3dist(pdfminer.six)
Recommends: python3dist(psycopg2)
Recommends: python3dist(pypng)
Recommends: python3dist(pyshp)
Recommends: python3dist(requests)
Recommends: python3dist(sas7bdat)
Recommends: python3dist(savReaderWriter)
Recommends: python3dist(tabulate)
Recommends: python3dist(vobject)
Recommends: python3dist(wcwidth)
Recommends: python3dist(xlrd)
Recommends: python3dist(xport)

%description -n python3-%{srcname}
VisiData is an interactive multitool for tabular data. It combines the clarity
of a spreadsheet, the efficiency of the terminal, and the power of Python, into
a lightweight utility which can handle millions of rows with ease.


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%files
%{_bindir}/visidata
%{_bindir}/vd
%{_mandir}/man1/vd.1*

%files -n python3-%{srcname}
%doc README.md
%license LICENSE.gpl3
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Oct 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version (#1887632)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.2-2
- Fix issues from review

* Tue Mar 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.2-1
- Initial package.
