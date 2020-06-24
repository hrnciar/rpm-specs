%global srcname PyLEMS
%global libname pylems

# Most tests try to download files from other github repos, so we cannot use them
%global run_tests 0

%global _description \
A LEMS (http://lems.github.io/LEMS) simulator written in Python which can be \
used to run NeuroML2 (http://neuroml.org/neuroml2.php) models.


Name:           python-%{srcname}
Version:        0.5.0
Release:        2%{?dist}
Summary:        LEMS interpreter implemented in Python

License:        LGPLv3

# Use github source. Pypi source does not include license and examples.
URL:            https://github.com/LEMS/%{libname}/
Source0:        https://github.com/LEMS/%{libname}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist lxml}
Requires:  %{py3_dist lxml}
Requires:  %{py3_dist matplotlib}
Requires:  %{py3_dist numpy}
%if %{run_tests}
BuildRequires:  %{py3_dist nose}
%endif
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%package doc
Summary: %{summary}

%description doc
%{_description}


%prep
%autosetup -n %{libname}-%{version}

# remove shebang
sed -i '1d' lems/dlems/exportdlems.py

%build
%py3_build

%install
%py3_install

%check

%if %{run_tests}
# From test*sh scripts in the source and .travis.yml

nosetests-3
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/apitest.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/apitest2.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/loadtest.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} lems/dlems/exportdlems.py

%endif

%files -n python3-%{srcname}
%license LICENSE.lesser
%doc README.md
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info
%{python3_sitelib}/lems
%{_bindir}/%{libname}

%files doc
%license LICENSE.lesser
%doc README.md examples

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-1
- Update to new release
- remove py2 bits

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.9.1-1
- Initial build
