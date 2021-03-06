# Generated by go2rpm 1
%bcond_without check

# https://github.com/xlzd/gotp
%global goipath         github.com/xlzd/gotp
%global commit          c8557ba2c11930b3069b31bfd80f38cc774cc68a

%gometa

%global common_description %{expand:
Golang OTP(One-Time Password) Library.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Golang OTP(One-Time Password) Library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Wed Jul 22 17:41:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200903gitc8557ba
- Initial package
