# Generated by go2rpm
%bcond_without check

# https://github.com/kr/text
%global goipath         github.com/kr/text
Version:                0.1.0

%gometa

%global common_description %{expand:
Miscellaneous functions for formatting text.}

%global golicenses      License
%global godocs          Readme Readme-colwriter Readme-mc

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        3%{?dist}
Summary:        Miscellaneous functions for formatting text

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/kr/pty)

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .
mv colwriter/Readme Readme-colwriter
mv mc/Readme Readme-mc

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/go-mc %{goipath}/mc

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 23:34:55 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Release 0.1.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.18.git6807e77
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.git6807e77
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.20131111git6807e77
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git6807e77
- Polish the spec file
  related: #1248175

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git6807e77
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git6807e77
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git6807e77
- Update to spec-2.1
  related: #1248175

* Wed Jul 29 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git6807e77
- Update of spec file to spec-2.0
  resolves: #1248175

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git6807e77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 19 2014 Jan Chaloupka <jchaloup@fedoraproject.org> - 0-0.3.git6807e77
- add golang version with necessary golang macros
- quiet setup

* Thu Sep 11 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.git6807e77
- gopath defined in golang package
- preserve timestamps while copying source files
- attrs not needed
- devel description update
- include check section
- get rid of files listed twice warning for doc files
- noarch
- needs kr/pty as BR
- chmod wrap.go to 644 (needs to be upstreamed)

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.git6807e77
- First package for Fedora.

