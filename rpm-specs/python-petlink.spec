%global srcname petlink

%global desc %{expand: \
Decode and encode Petlink data streams (32 and 64 bit)
The encode and decode routines are written in C and are wrapped with Python.}

Name:           python-%{srcname}
Version:        0.3.4
Release:        8%{?dist}
Summary:        Decode and encode Petlink data streams (32 and 64 bit)

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source
# https://raw.githubusercontent.com/spedemon/petlink/master/LICENSE
Source1:        LICENSE.%{srcname}

BuildRequires:  gcc

%description
%{desc}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist simplewrap} >= 0.3.3
Requires:       %{py3_dist numpy}
Requires:       %{py3_dist simplewrap} >= 0.3.3
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}
cp -v %{SOURCE1} LICENSE

rm -rfv %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}-%{version}-py3.?.egg-info
%{python3_sitearch}/%{srcname}

%changelog
* Mon Oct 05 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.4-8
- Explicitly require setuptools
- drop py2 subpackage

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.4-1
- Update to 0.3.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.2-1
- Rename license file to LICENSE as per reviewer suggestion

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.2-1
- Initial build
