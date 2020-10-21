%global pypi_name blurb

Name:           python-%{pypi_name}
Version:        1.0.8
%global uversion %{version}
Release:        2%{?dist}
Summary:        Command-line tool to manage CPython Misc/NEWS.d entries

License:        BSD
URL:            https://github.com/python/core-workflow/tree/master/blurb
Source0:        %pypi_source %{pypi_name} %{uversion}
# flit 3.0.0 requires pyproject.toml file instead of flit.ini.
# This can be removed once upstream PR is merged.
# https://github.com/python/core-workflow/pull/375
Patch0:         https://github.com/python/core-workflow/commit/0c98be37887a0ec00d181ed253e1fd031783d270.patch
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Blurb is a tool designed to rid CPython core development of the scourge of
Misc/NEWS conflicts.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       %{pypi_name} == %{version}-%{release}

# Entrypoints
Requires:       python3-setuptools

# Calls git in subprocess
Requires:       /usr/bin/git

%description -n python3-%{pypi_name}
Blurb is a tool designed to rid CPython core development of the scourge of
Misc/NEWS conflicts.

%prep
%autosetup -n %{pypi_name}-%{uversion}

# script in site-packages
sed -i '1d' %{pypi_name}.py
chmod -x %{pypi_name}.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/blurb

%changelog
* Thu Oct 01 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.0.8-2
- Backport patch to replace flit.ini with pyproject.toml needed by flit 3.0.0
- Convert spec to use pyproject-rpm-macros

* Thu Sep 24 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.0.8-1
- Update to 1.0.8
- Only require /usr/bin/git, not full git

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-1
- Update to upstream 1.0.7 (#1598195)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Petr Viktorin <pviktori@redhat.com> - 1.0.5-1
- Update to upstream 1.0.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1.post1
- rebuilt
