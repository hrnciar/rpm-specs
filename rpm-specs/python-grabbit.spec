# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
%if 0%{?fedora} < 30
%global with_py2 1
%else
%global with_py2 0
%endif

%global srcname     grabbit
%global sum     Get grabby with file trees

%global _description %{expand: \
Grabbit is a lightweight Python package for simple queries over filenames
within a project. It is geared towards projects or applications with highly
structured filenames that allow useful queries to be performed without having
to inspect the file metadata or contents.
}

Name:       python-%{srcname}
Version:    0.2.6
Release:    7%{?dist}
Summary:    %{sum}

License:    MIT
URL:        https://github.com/grabbles/%{srcname}
Source0:    https://github.com/grabbles/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz


BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist inflect}
BuildRequires:  %{py3_dist pytest-capturelog}
Requires:       %{py3_dist pandas}
Requires:       %{py3_dist six}
Requires:       %{py3_dist hdfs}
Requires:       %{py3_dist inflect}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%if %{with_py2}
%package -n python2-%{srcname}
Summary:        %{sum}
BuildRequires:  python2-devel
BuildRequires:  %{py2_dist setuptools}
BuildRequires:  %{py2_dist pytest}
BuildRequires:  %{py2_dist six}
BuildRequires:  %{py2_dist inflect}
BuildRequires:  %{py2_dist pytest-capturelog}
Requires:       %{py2_dist pandas}
Requires:       %{py2_dist six}
Requires:       %{py2_dist hdfs}
Requires:       %{py2_dist inflect}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{_description}
%endif

%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info

%build
%if %{with_py2}
%py2_build
%endif
%py3_build


%install
%if %{with_py2}
%py2_install
%endif
%py3_install

%check
%if %{with_py2}
PYTHONPATH=. py.test-2
%endif
PYTHONPATH=. py.test-3

%files -n python3-%{srcname}
%license LICENSE
%doc README.md examples
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}/

%if %{with_py2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md examples
%{python2_sitelib}/%{srcname}-%{version}-py2.?.egg-info
%{python2_sitelib}/%{srcname}/
%endif


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.6-1
- Update to new pstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.5-1
- Update to latest release
- Use conditional to use common spec for all releases
- Include LICENSE

* Thu Nov 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-5
- Subpackage python2-grabbit has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jul 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-4
- use py.test

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-1
- Update to 0.2.0
- Update as per review comments

* Mon Jan 15 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.0-1
- Initial build
