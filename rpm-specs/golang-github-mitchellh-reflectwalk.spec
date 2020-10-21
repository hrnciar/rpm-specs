# Generated by go2rpm
%bcond_without check

# https://github.com/mitchellh/reflectwalk
%global goipath         github.com/mitchellh/reflectwalk
Version:                1.0.1

%gometa

%global common_description %{expand:
Reflectwalk is a Go library for "walking" a value in Go using reflection, in the
same way a directory tree can be "walked" on the filesystem. Walking a complex
structure can allow you to do manipulations on unknown structures such as those
decoded from JSON.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        5%{?dist}
Summary:        Go library for "walking" complex structures, similar to walking a filesystem

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 23:27:27 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Release 1.0.1

* Sat Apr 06 17:38:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Release 1.0.0 (#1695317)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.giteecf4c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.8.giteecf4c7
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.giteecf4c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.giteecf4c7
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.giteecf4c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.giteecf4c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.giteecf4c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.2.giteecf4c7
- Disable tests
  related: #1410150

* Wed Jan 04 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.giteecf4c7
- First package for Fedora
  resolves: #1410150
