# Generated by go2rpm
%bcond_without check

# https://github.com/kdar/factorlog
%global goipath         github.com/kdar/factorlog
%global commit          d5b6afb8b4fe1ee3fb6d99ba3a75781fa50a9f7c

%gometa

%global common_description %{expand:
FactorLog is a fast logging infrastructure for Go that provides numerous logging
functions for whatever your style may be. It could easily be a replacement for
Go's log in the standard library (though it doesn't support functions such as
SetFlags()).

It has a modular formatter interface, and even have a GELF and glog formatter in
the contrib.}

%global golicenses      LICENSE
%global godocs          examples README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.19%{?dist}
Summary:        Logging infrastructure for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/mgutz/ansi)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 17:58:27 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.17.20190602gitd5b6afb
- Bump to commit d5b6afb8b4fe1ee3fb6d99ba3a75781fa50a9f7c

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.git814d8f7
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git814d8f7
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git814d8f7
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git814d8f7
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git814d8f7
- Update to spec-2.1
  related: #1254593

* Wed Aug 12 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git814d8f7
- Update spec file to spec-2.0
  resolves: #1254593

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git814d8f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Bug 1092057 - Initial fedora package
