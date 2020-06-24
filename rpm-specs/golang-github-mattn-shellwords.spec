# Generated by go2rpm
%bcond_without check

# https://github.com/mattn/go-shellwords
%global goipath         github.com/mattn/go-shellwords
Version:                1.0.10

%gometa

%global common_description %{expand:
Parse line as shell words.}

%global golicenses      LICENSE
%global godocs          _example README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Parse line as shell words

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
* Sat Feb 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.10-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.6-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 01:02:37 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.5-1
- Release 1.0.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.3-7
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-5
- Re-template against More Go Packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-3
- Tweak versioning macros.

* Sat Aug 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-2
- Fix bug in spec unpacking.

* Sat Aug 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-1
- Switch to released version

* Fri Aug 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.git9858af9
- Initial package for Fedora
