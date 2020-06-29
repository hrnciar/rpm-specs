%global srcname pypillowfight

Name:           python-%{srcname}
Version:        0.3.0
Release:        3%{?dist}
Summary:        Various image processing algorithms

License:        GPLv2+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight
# PyPI tarball does not include tests.
#Source0:        https://files.pythonhosted.org/packages/source/p/%%{srcname}/%%{srcname}-%%{version}.tar.gz
Source0:        https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/-/archive/%{version}/libpillowfight-%{version}.tar.gz
# https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/issues/15
Source1:        images.tar.xz
# Because Fedora 32-bit does not necessarily support SSE2.
Patch0001:      0001-Do-not-override-compile-args.patch

%global _description \
Library containing various image processing algorithms: Automatic Color \
Equalization, Unpaper's algorithms, Stroke Width Transformation, etc.

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose >= 1.0
BuildRequires:  python3-pillow

Requires:       python3-pillow%{?_isa}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n libpillowfight-%{version} -p1
%setup -D -T -n libpillowfight-%{version} -q -a 1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

echo "#define INTERNAL_PILLOWFIGHT_VERSION \"%{version}\"" > src/pillowfight/_version.h


%build
%py3_build


%install
%py3_install


%check
# https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight/issues/11
%ifarch i686
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    nosetests-3 -v -P tests -e test_swt2
%else
%ifarch aarch64 ppc64le
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    nosetests-3 -v -P tests -I 'tests_swt.py' -I 'tests_canny.py'
%else
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    nosetests-3 -v -P tests
%endif
%endif


%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitearch}/pillowfight
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- New upstream release.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-2
- Fix license and requires.

* Wed Dec 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Initial package.
