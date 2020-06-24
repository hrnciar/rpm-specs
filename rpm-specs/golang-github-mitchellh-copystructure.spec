# Generated by go2rpm
%bcond_without check

# https://github.com/mitchellh/copystructure
%global goipath         github.com/mitchellh/copystructure
Version:                1.0.0

%gometa

%global common_description %{expand:
Copystructure is a Go library for deep copying values in Go.

This allows you to copy Go values that may contain reference values such as
maps, slices, or pointers, and copy their data as well instead of just their
references.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        4%{?dist}
Summary:        Go library for deep copying values in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/mitchellh/reflectwalk)

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

# Remove in F33
# Remove erroneous glide.lock folder
%pretrans devel -p <lua>
path = "%{gopath}/src/%{goipath}/glide.lock"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path)
end

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 15:32:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2
- Update to new macros

* Wed Apr 03 20:23:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Release 1.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitcdac825
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.7.gitcdac825
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitcdac825
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.gitcdac825
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitcdac825
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitcdac825
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitcdac825
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jan 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.gitcdac825
- First package for Fedora
  resolves: #1410401
