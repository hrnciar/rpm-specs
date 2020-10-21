# Generated by go2rpm 1
%bcond_without check

# https://github.com/stacktitan/smb
%global goipath         github.com/stacktitan/smb
%global commit          da9a425dceb89b24a6e823c9069349b165b3b6de

%gometa

%global common_description %{expand:
An SMB library in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        SMB library in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/md4)

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200518gitda9a425
- Initial package

