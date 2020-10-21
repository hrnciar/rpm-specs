# Generated by go2rpm
%bcond_without check

# https://github.com/Azure/go-ansiterm
%global goipath         github.com/Azure/go-ansiterm
%global commit          d6e3b3328b783f23731bc4d058875b0371ff8109

%gometa

%global common_description %{expand:
This is a cross platform Ansi Terminal Emulation library. It reads a stream of
Ansi characters and produces the appropriate function calls. The results of the
function calls are platform dependent.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Go package for ANSI terminal emulation in Windows

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Go 1.15: https://github.com/golang/go/issues/32479
Patch0:         0001-Convert-int-to-string-using-rune.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Aug 22 21:16:28 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20190627gitd6e3b33
- Fix FTBFS

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 21:18:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627gitd6e3b33
- Initial package
