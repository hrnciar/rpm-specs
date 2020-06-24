# Generated by go2rpm 1
%bcond_without check

# https://github.com/valyala/goloris
%global goipath         github.com/valyala/goloris
%global commit          a59fafb2dd6c401d7cb50964dde3ffafbd456451

%gometa

%global common_description %{expand:
Slowloris for NGINX DoS. Written in go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           goloris
Version:        0
Release:        0.1%{?dist}
Summary:        Slowloris for NGINX DoS

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/goloris %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200316gita59fafb
- Initial package for Fedora

