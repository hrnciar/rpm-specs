%global srcname mplcursors

Name:           python-%{srcname}
Version:        0.3
Release:        3%{?dist}
Summary:        Interactive data selection cursors for Matplotlib

License:        MIT
URL:            https://github.com/anntzer/mplcursors
Source0:        %pypi_source
Patch0001:      https://github.com/anntzer/mplcursors/commit/6f089d9a4d05e031ea443f7543c8f9b1c62e9135.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(matplotlib) >= 3.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pytest)

%description
mplcursors – Interactive data selection cursors for Matplotlib


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
 
Requires:       python3dist(matplotlib) >= 2.1

%description -n python3-%{srcname}
mplcursors – Interactive data selection cursors for Matplotlib


%package -n python-%{srcname}-doc
Summary:        mplcursors documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-gallery) >= 0.1.13
BuildRequires:  python3dist(pandas)

%description -n python-%{srcname}-doc
Documentation for mplcursors


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info and files
rm -rf %{srcname}.egg-info vendor


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD}/build/lib sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{python3} -m pytest


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst examples/README.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}.pth
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info


%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Fri Aug 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2-2
- Remove vendored source code

* Fri Aug 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2-1
- Initial package.
