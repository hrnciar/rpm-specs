# Generated by go2rpm
%bcond_without check

# https://github.com/aybabtme/rgbterm
%global goipath         github.com/aybabtme/rgbterm
%global commit          cc83f3b3ce5911279513a46d6d3316d67bedaa54

%gometa

%global common_description %{expand:
Package rgbterm colorizes bytes and strings using RGB colors, for a full range
of pretty terminal strings.

Beyond the traditional boring 16 colors of your terminal lie an extended set of
256 pretty colors waiting to be used. However, they are weirdly encoded; simply
asking for an RGB color is much more convenient! }

%global golicenses      LICENSE LICENSE-rainbow
%global godocs          README.md README-rainbow.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        RGB colors for your terminal

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
mv rainbow/LICENSE LICENSE-rainbow
mv rainbow/README.md README-rainbow.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 22:55:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190624gitcc83f3b
- Initial package
