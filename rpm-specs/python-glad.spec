%global srcname glad

Name:           python-%{srcname}
Version:        0.1.33
Release:        4%{?dist}
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator

License:        MIT
URL:            https://github.com/Dav1dde/glad
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%package -n     %{srcname}
Summary:        %{summary}

Requires:       python3dist(glad)

%description -n %{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(setuptools)

%description -n python3-%{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Fix shebang
sed -i -e '/^#!\//, 1d' %{srcname}/__main__.py


%build
%py3_build


%install
%py3_install


%files -n %{srcname}
%{_bindir}/glad

%files -n python3-%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.33-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.33-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.33-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.31-1
- Update to latest version

* Fri Jun 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.30-1
- Initial package.
