# Generated by go2rpm 1
%bcond_without check

# https://github.com/gizak/termui
%global goipath         github.com/gizak/termui
Version:                3.1.0

%gometa

%global common_description %{expand:
termui is a cross-platform and fully-customizable terminal dashboard and widget
library built on top of termbox-go. It is inspired by blessed-contrib and
tui-rs and written purely in Go.

Features:

- Several premade widgets for common use cases
- Easily create custom widgets
- Position widgets either in a relative grid or with absolute coordinates
- Keyboard, mouse, and terminal resizing events
- Colors and styling
}

%global golicenses      LICENSE
%global godocs          _examples README.md CHANGELOG.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang terminal dashboard

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/mitchellh/go-wordwrap)
BuildRequires:  golang(github.com/nsf/termbox-go)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 05:21:29 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.1.0-1
- Initial package

