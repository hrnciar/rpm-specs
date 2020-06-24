# Generated by go2rpm
%bcond_without check

# https://github.com/glycerine/go-unsnap-stream
%global goipath         github.com/glycerine/go-unsnap-stream
%global commit          f9677308dec2b35e76737f9713df328ad11b1fea

%gometa

%global common_description %{expand:
Small golang library for decoding the snappy streaming format.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Small Go library for decoding the snappy streaming format

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/snappy)

%if %{with check}
# Tests
# It's a fork: I'd rather use the original from smartystreets
# which is updated and already packaged.
# BuildRequires: golang(github.com/glycerine/goconvey/convey)
BuildRequires: golang(github.com/smartystreets/goconvey/convey)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

# Convert to use the original from smartystreets
# which is updated and already packaged, instead of the fork.
find . -name "*.go" -exec sed -i "s|github.com/glycerine/goconvey|github.com/smartystreets/goconvey|" "{}" +;

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 23:07:53 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190307gitf967730
- Update to new macros

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190307gitf967730
- First package for Fedora