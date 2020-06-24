# Generated by go2rpm
%bcond_without check

# https://github.com/lithammer/dedent
%global goipath         github.com/lithammer/dedent
Version:                1.1.0

%gometa

%global common_description %{expand:
Remove any common leading whitespace from multiline strings.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Remove any common leading whitespace from multiline strings

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 20:56:51 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Initial package
