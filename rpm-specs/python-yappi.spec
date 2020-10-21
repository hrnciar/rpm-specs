%global srcname yappi

Name:           python-%{srcname}
Version:        1.2.5
Release:        1%{?dist}
Summary:        Yet Another Python Profiler, supports Multithread/CPU time profiling

License:        MIT
URL:            https://github.com/sumerc/yappi
Source0:        https://files.pythonhosted.org/packages/source/y/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc

%description
Yappi, Yet Another Python Profiler, provides multithreading and cpu-time
support to profile python programs.

%package -n python3-%{srcname}
Summary:        Yet Another Python Profiler, supports Multithread/CPU time profiling.

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname}
Yappi, Yet Another Python Profiler, provides multithreading and cpu-time
support to profile python programs.

%prep
%autosetup -n %{srcname}-%{version} -S git

%build
%py3_build

%install
%py3_install
mv %{buildroot}%{_bindir}/%{srcname} %{buildroot}%{_bindir}/%{srcname}-%{python3_version}
ln -s %{srcname}-%{python3_version} %{buildroot}%{_bindir}/%{srcname}-3
ln -s %{srcname}-3 %{buildroot}%{_bindir}/%{srcname}

%check
export PATH=$PATH:%{buildroot}/usr/bin
export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%{__python3} tests/test_functionality.py
%{__python3} tests/test_hooks.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{srcname}.py*
%{python3_sitearch}/_%{srcname}*.so
%{python3_sitearch}/__pycache__/%{srcname}*
%{python3_sitearch}/%{srcname}-*.egg-info
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-3*

%changelog
* Fri Aug 28 2020 Alfredo Moralejo <amoralej@redhat.com> - 1.2.5-1
- Update to 1.2.5 version
- Removed python2 subpackage

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.0-1
- Initial version
