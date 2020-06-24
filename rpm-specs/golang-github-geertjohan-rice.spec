# Generated by go2rpm
%bcond_without check

# https://github.com/GeertJohan/go.rice
%global goipath         github.com/GeertJohan/go.rice
Version:                1.0.0

%gometa

%global common_description %{expand:
Go.rice is a Go package that makes working with resources such as
html,js,css,images,templates, etc very easy.}

%global golicenses      LICENSE
%global godocs          example AUTHORS README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Go.rice is a Go package that makes working with resources such as html,js,css,images,templates, etc very easy

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/akavel/rsrc/binutil)
BuildRequires:  golang(github.com/akavel/rsrc/coff)
BuildRequires:  golang(github.com/daaku/go.zipexe)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/GeertJohan/go.incremental)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/nkovacs/streamquote)
BuildRequires:  golang(github.com/valyala/fasttemplate)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in rice; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc example AUTHORS README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 23:02:39 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package

