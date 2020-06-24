# Generated by go2rpm
%bcond_without check

# https://github.com/VividCortex/gohistogram
%global goipath         github.com/VividCortex/gohistogram
Version:                1.0.0

%gometa

%global common_description %{expand:
This package provides Streaming Approximate Histograms for efficient quantile
approximations.

The histograms in this package are based on the algorithms found in Ben-Haim &
Yom-Tov's A Streaming Parallel Decision Tree Algorithm. Histogram bins do not
have a preset size. As values stream into the histogram, bins are dynamically
added and merged.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Streaming approximate histograms in Go

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 01:15:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package