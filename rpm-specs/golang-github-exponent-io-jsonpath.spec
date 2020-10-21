# Generated by go2rpm
%bcond_without check

# https://github.com/exponent-io/jsonpath
%global goipath         github.com/exponent-io/jsonpath
%global commit          d6023ce2651d8eafb5c75bb0c7167536102ec9f5

%gometa

%global common_description %{expand:
This package extends the json.Decoder to support navigating a stream of JSON
tokens. You should be able to use this extended Decoder places where a
json.Decoder would have been used.

This Decoder has the following enhancements:
 - The Scan method supports scanning a JSON stream while extracting particular
   values along the way using PathActions.
 - The SeekTo method supports seeking forward in a JSON token stream to a
   particular path.
 - The Path method returns the path of the most recently parsed token.
 - The Token method has been modified to distinguish between strings that are
   object keys and strings that are values. Object key strings are returned as
   the KeyString type rather than a native string.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Extend the Go runtime's json.Decoder

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 04:29:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190629gitd6023ce
- Initial package
