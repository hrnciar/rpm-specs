%global srcname octave-kernel
%global srcname_ octave_kernel

Name:           python-%{srcname}
Version:        0.32.0
Release:        2%{?dist}
Summary:        A Jupyter kernel for Octave

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname_}
Source0:        %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  gnuplot
BuildRequires:  octave

%{?python_enable_dependency_generator}

%global _description \
A Jupyter kernel for Octave.

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(metakernel) >= 0.24.0
BuildRequires:  python3dist(jupyter-client) >= 4.3.0
BuildRequires:  python3dist(ipykernel)

BuildRequires:  python3dist(jupyter-kernel-test)

Requires:       octave

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname_}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    JUPYTER_PATH="%{buildroot}%{_datadir}/jupyter" \
        %{python3} test_octave_kernel.py -v


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname_}
%{python3_sitelib}/%{srcname_}-%{version}-py%{python3_version}.egg-info
%{_datadir}/jupyter/kernels/octave


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.32.0-1
- Update to latest version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.31.1-2
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.31.1-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.31.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.31.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.31.0-2
- Fix tests with Octave 5

* Sun Jun 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.31.0-1
- Update to latest version

* Thu May 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.30.3-1
- Update to latest version

* Mon May 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.30.2-1
- Update to latest version

* Tue Apr 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.29.0-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.28.4-1
- Update to latest version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.28.3-3
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.28.3-2
- Force Python 3 for kernel startup (for old Jupyter client.)

* Thu Mar 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.28.3-1
- Initial package release.
