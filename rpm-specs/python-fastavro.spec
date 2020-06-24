# Fail only on i686 for some reason. Issue filed upstream:
# https://github.com/tebeka/fastavro/issues/147
%bcond_with tests

%global srcname     fastavro
%global sum     Fast Avro for Python
%global _description %{expand: \
Apache Avro is a data serialization system. The current Python avro package is
packed with features but dog slow. fastavro is less feature complete than avro,
however it is much faster.}

Name:       python-%{srcname}
Version:    0.23.3
Release:    2%{?dist}
Summary:    %{sum}

# https://github.com/tebeka/fastavro/issues/60
# Apache avro is under ASL 2.0
# https://avro.apache.org/docs/1.8.2/api/cpp/html/ResolvingReader_8hh_source.html etc
License:    ASL 2.0
URL:        https://github.com/%{srcname}/%{srcname}
Source0:    %pypi_source %{srcname}

BuildRequires:  gcc

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
Requires:       %{py3_dist python-snappy}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%package doc
Summary:        %{sum}
%description doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info
# We don't run the flake8 and manifest check tests so we remove this from the
# setup.py file to prevent it from trying to fetch stuff from pypi
sed -i "/tests_require=/d" setup.py

# Remove the already generated C files so we generate them ourselves
find fastavro/ -name "*.c" -print -delete

%build
export FASTAVRO_USE_CYTHON=1
%py3_build

pushd docs
    PYTHONPATH=../ make html man
    pushd _build/html
        rm .buildinfo -f || exit -1
        sed -i 's/\r$//' objects.inv
        iconv -f iso8859-1 -t utf-8 objects.inv > objects.inv.conv && mv -fv objects.inv.conv objects.inv
    popd
popd


%install
export FASTAVRO_USE_CYTHON=1

%py3_install

# Install man page
install -v -p -D -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1 || exit -1

%check
%if %{with tests}
PYTHONPATH=%{buildroot}%{python3_sitearch} pytest-3 tests
%endif

%files -n python3-%{srcname}
%license NOTICE.txt
%{python3_sitearch}/%{srcname}-%{version}-py?.?.egg-info
%{python3_sitearch}/%{srcname}/
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.*

%files doc
%doc README.md
%license NOTICE.txt
%doc docs/_build/html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.23.3-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.23.3-1
- Update to latest release
- Remove py2 bits

* Sun Feb 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.22.9-1
- Update to 0.22.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 9 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.22.7-1
- Update to 0.22.7
- Remove Cython version constraint, F29 is no more maintained

* Sat Oct 12 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.22.5-1
- Update to 0.22.5

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.22.4-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.22.4-1
- Update to 0.22.4

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.22.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 0.22.2-1
- New Upstream version

* Fri May 31 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 0.21.24-1
- Update to 0.19.8

* Mon May 13 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.21.23-1
- Update to latest release

* Sun Feb 03 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.21.17-1
- Update to latests upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.21.13-1
- Disable py3 on F30+
- Update to latest release
- Use pypi source

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.19.8-2
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.19.8-1
- Update to 0.19.8

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.19.6-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.19.6-1
- Update to new release
- Tests still failing for i686 so disabling

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.17.3-3
- Re-enable tests for testing

* Mon Jan 22 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.17.3-2
- Disable tests temporarily - fail on i686 only. Issue filed upstream.

* Sun Jan 21 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.17.3-1
- Update for review (rhbz#1534787)
- Update to latest upstream release
- Generate separate doc subpackage for docs
- Install man page
- Rectify license
- Fix tests

* Mon Jan 15 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.17.1-1
- Initial build
