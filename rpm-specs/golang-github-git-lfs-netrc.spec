# Generated by go2rpm
%bcond_without check

# https://github.com/git-lfs/go-netrc
%global goipath         github.com/git-lfs/go-netrc
%global commit          e0e9ca483a183481412e6f5a700ff20a36177503

%gometa

%global common_description %{expand:
A Golang package for reading and writing netrc files. This package can
parse netrc files, make changes to them, and then serialize them back to
netrc format, while preserving any whitespace that was present in the
source file.}

%global golicenses      LICENSE
%global godocs          README.md examples

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Golang package for reading and writing netrc files

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 16:52:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180827gite0e9ca4
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gite0e9ca4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.2.gite0e9ca4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jun 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180827gite0e9ca4
- Initial package for Fedora
