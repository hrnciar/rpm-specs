# Generated by go2rpm 1
%bcond_without check

# https://github.com/masterzen/winrm
%global goipath         github.com/masterzen/winrm
%global commit          c42b5136ff886aff9dba40fb3670281f0d583db8

%gometa

%global common_description %{expand:
Command-line tool and library for Windows remote command execution in Go.}

%global golicenses      LICENSE
%global godocs          README.md development/sample_requests.txt

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Command-line tool and library for Windows remote command execution

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/Azure/go-ntlmssp)
BuildRequires:  golang(github.com/ChrisTrenkamp/goxpath)
BuildRequires:  golang(github.com/ChrisTrenkamp/goxpath/tree)
BuildRequires:  golang(github.com/ChrisTrenkamp/goxpath/tree/xmltree)
BuildRequires:  golang(github.com/gofrs/uuid)
BuildRequires:  golang(github.com/masterzen/simplexml/dom)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jul 29 19:59:05 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20200729gitc42b513
- Bump to commit c42b5136ff886aff9dba40fb3670281f0d583db8

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200406git1d17eaf
- Initial package

