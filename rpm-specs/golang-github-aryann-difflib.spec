# Generated by go2rpm 1
%bcond_without check

# https://github.com/aryann/difflib
%global goipath         github.com/aryann/difflib
%global commit          e206f873d14a916d3d26c40ab667bca123f365a3

%gometa

%global common_description %{expand:
difflib is a simple library written in Go for diffing two sequences of text.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Library for diffing two sequences of text

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in difflib_server; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

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
* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200406gite206f87
- Initial package

