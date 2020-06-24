# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
# http://rpm.org/user_doc/conditional_builds.html
%if 0%{?fedora} >= 30
# disabled by default
%bcond_with py2
%else
%bcond_without py2 0
%endif

%global srcname pygiftiio

%global desc %{expand: \
GIFTI is an XML-based file format for cortical surface data. This reference IO
implementation is developed by the Neuroimaging Informatics Technology
Initiative (NIfTI).}

Name:           python-%{srcname}
Version:        1.0.4
Release:        8%{?dist}
Summary:        Python bindings for Gifti

License:        GPLv2
URL:            https://www.nitrc.org/frs/?group_id=75
Source0:        https://www.nitrc.org/frs/download.php/1285/%{srcname}-%{version}.tar.gz
Source1:        https://www.nitrc.org/frs/download.php/261/gifti_write_example.py
Source2:        https://www.nitrc.org/frs/download.php/260/gifti_read_example.py

BuildArch:      noarch

%description
%{desc}

%if %{with py2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
Requires:       gifticlib-devel
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       gifticlib-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}
cp -v %{SOURCE1} .
cp -v %{SOURCE2} .

%build
# Nothing to do

%install
# Put things where they belong
install -D -m 0644 %{srcname}.py -t %{buildroot}/%{python3_sitelib}/
%if %{with py2}
install -D -m 0644 %{srcname}.py -t %{buildroot}/%{python2_sitelib}/
%endif

%check
# No tests

%if %{with py2}
%files -n python2-%{srcname}
%license LICENSE.GPL
%doc gifti_write_example.py gifti_read_example.py
%{python2_sitelib}/%{srcname}.py
%{python2_sitelib}/%{srcname}.pyc
%{python2_sitelib}/%{srcname}.pyo
%endif

%files -n python3-%{srcname}
%license LICENSE.GPL
%doc gifti_write_example.py gifti_read_example.py
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.cpython-3*.opt-1.pyc
%{python3_sitelib}/__pycache__/%{srcname}.cpython-3*.pyc

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.4-2
- Fix file list to cater to different py3 versions

* Sun Nov 18 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.4-1
- Only install py2 files conditionally
- Initial build
- Correct license
