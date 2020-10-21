%{?python_enable_dependency_generator}

%global modname ssh2-python

Name:           python-%{modname}
Version:        0.15.0
Release:        10%{?dist}
Summary:        Super fast SSH library - bindings for libssh2

License:        LGPLv2+
URL:            https://github.com/ParallelSSH/ssh2-python
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libssh2-devel

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
# No bundled libs
rm -vrf libssh2

# Remove pre-generated sources
rm $(grep -rl '/\* Generated by Cython')

%build
export HAVE_AGENT_FWD=0
%py3_build

%install
%py3_install

#check
# Requires real SSH server

%files -n python3-%{modname}
%license COPYING LICENSE
%doc README.rst Changelog.rst
%{python3_sitearch}/ssh2_python-*.egg-info/
%{python3_sitearch}/ssh2/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.15.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.15.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.15.0-3
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.0-1
- Initial package

