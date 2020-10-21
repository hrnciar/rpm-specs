# Generated by go2rpm
%bcond_without check

# https://github.com/oschwald/geoip2-golang
%global goipath         github.com/oschwald/geoip2-golang
Version:                1.4.0
# test data for the non-exported git submodule
%global dataurl         https://github.com/maxmind/MaxMind-DB
%global dataref         13c25fcb6f50fdd0ec8286b4d540a45a20e28b0d

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-oschwald-geoip2-golang-devel < 1.3.0-2
}

%global common_description %{expand:
This library reads MaxMind GeoLite2 and GeoIP2 databases.

This library is built using the Go maxminddb reader. All data for the database
record is decoded using this library. If you only need several fields, you may
get superior performance by using maxminddb's Lookup directly with a result
struct that only contains the required fields. (See example_test.go in the
maxminddb repository for an example of this.)}

%global golicenses      LICENSE test-data/LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Unofficial MaxMind GeoIP2 Reader for Go

# Code: ISC; Test data: CC-BY-SA 3.0
License:        ISC and CC-BY-SA
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{dataurl}/archive/%{dataref}/MaxMind-DB-%{dataref}.tar.gz

BuildRequires:  golang(github.com/oschwald/maxminddb-golang)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
# extract test data to the right location
pushd test-data
tar -xzf %{SOURCE1}
mv MaxMind-DB-%{dataref}/* ./
rm -r MaxMind-DB-%{dataref}
popd

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.0-1
- Update to version 1.4.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-2
- Add Obsoletes for old name

* Mon Jun 03 17:01:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-1
- Release 1.3.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-4
- Use standard GitHub SourceURL again for consistency between releases.
- Use forgeautosetup instead of gosetup.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-3
- Update to spec 3.0 and enable tests.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-1
- Update to version 1.2.1.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-1
- Update to version 1.2.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Mon Mar 13 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1.20170314.git0fd242d
- First package for Fedora
