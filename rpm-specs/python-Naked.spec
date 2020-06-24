# Created by pyp2rpm-3.2.3
%global pypi_name Naked
%global _description Naked is a new Python command line application framework \
                     that makes creating command line options and sub-commands \
                     simpler.

Name:           python-%{pypi_name}
Version:        0.1.31
Release:        13%{?dist}
Summary:        A command line application framework

License:        MIT
URL:            http://naked-py.com
Source0:        https://files.pythonhosted.org/packages/source/N/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildArch:      noarch

%description
%{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Conflicts:      python2-%{pypi_name} < 0.1.31-8

Requires:       python3-Naked
Requires:       python3-PyYAML
Requires:       python3-requests
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
%{_description}


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

sed -i -e '1d' lib/Naked/templates/licenses.py
sed -i -e '1d' lib/Naked/templates/readme_md_file.py

%install
function update_scripts() {
    for f in $(find "${1}" -name '*.py*'); do
        if [ x"$(head -n1 "${f}")" == "x#!/usr/bin/env python" ]; then
            sed -i -e '1d' "${f}"
        fi
    done
    find "${1}" \( -name '*.c' -or -name '*.sh' \) -delete
}

%py3_install
update_scripts "%{buildroot}/%{python3_sitelib}/%{pypi_name}"


%files -n python3-%{pypi_name}
%license docs/LICENSE lib/Naked/templates/licenses.py
%doc docs/README.rst lib/Naked/templates/readme_md_file.py
%{_bindir}/naked
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-8
- Subpackage python2-Naked has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.31-5
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Gregory Hellings <greg.hellings@gmail.com> - 0.1.31-4
- Corrected spelling of Python 3 dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Gregory Hellings <greg.hellings@gmail.com> - 0.1.31-2
- Fixed description length
- Fixed executable file lint errors

* Mon Sep 25 2017 Gregory Hellings <greg.hellings@gmail.com> - 0.1.31-1
- Initial package.
